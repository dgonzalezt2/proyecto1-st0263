import httpx
import asyncio
import os
import shutil
import grpc
import filetransfer_pb2
import filetransfer_pb2_grpc

MAX_MESSAGE_LENGTH = 1024 * 1024 * 1024 # 1 GB en bytes
BASE_URL = 'http://34.31.203.46'

async def upload_request(file_size: int):
    async with httpx.AsyncClient() as client:
        for attempt in range(3):
            response = await client.get(f'{BASE_URL}/chunk-file?fileSizeInMb={file_size}')
            data = response.json()
            if 'error' not in data:
                return data
            else:
                print(f"Error en el intento {attempt + 1}: {data['error']}")
                if attempt < 2:
                    await asyncio.sleep(1)
        return data

async def upload_success(file_name: str, chunk_size: int, chunk_number: int):
    payload = {
        "fileName": file_name,
        "chunkSize": chunk_size,
        "totalChunks": chunk_number
    }
    async with httpx.AsyncClient() as client:
        for attempt in range(3):
            response = await client.post(f'{BASE_URL}/update-file', json=payload)
            response_data = response.json()
            if 'error' not in response_data:
                return response_data
            else:
                print(f"Error en el intento {attempt + 1}: {response_data['error']}")
                if attempt < 2:
                    await asyncio.sleep(1)
        return response_data

async def download_request(file_name: str):
    async with httpx.AsyncClient() as client:
        for attempt in range(3):
            response = await client.get(f'{BASE_URL}/get-file?fileName={file_name}')
            data = response.json()
            if 'error' not in data:
                return data
            else:
                print(f"Error en el intento {attempt + 1}: {data['error']}")
                if attempt < 2:
                    await asyncio.sleep(1)
        return data


def send_chunk(data_node: str, file_name: str, chunk_number: int, chunk_data: bytes):
    channel = grpc.insecure_channel(f'{data_node}:50051', options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ])
    stub = filetransfer_pb2_grpc.FileServiceStub(channel)
    response = stub.SendChunk(
        filetransfer_pb2.ChunkData(
            filename=file_name, chunk_number=chunk_number, chunk_data=chunk_data
        )
    )
    return response


def download_chunk(data_node: str, file_name: str, chunk_number: int):
    try:
        channel = grpc.insecure_channel(f'{data_node}:50051', options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
        ])
        stub = filetransfer_pb2_grpc.FileServiceStub(channel)
        response = stub.RequestChunk(
            filetransfer_pb2.ChunkRequest(filename=file_name, chunk_number=chunk_number)
        )

        dir_name = f'{file_name}_chunks'

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        with open(f"{dir_name}/{chunk_number}", 'wb') as f:
            f.write(response.chunk_data)

        print(f"Chunk {chunk_number} descargado.")

        return True
    except Exception as e:
        print(f"Error al descargar el chunk {chunk_number} del nodo {data_node}: {e}")
        return False


async def upload_file(file_name: str):
    try:
        file_size_mb = os.path.getsize(file_name) / 1_000_000

        print(f"El tamaño del archivo es: {file_size_mb} MB")

        partition_data = await upload_request(file_size_mb)

        if 'error' in partition_data:
            print(f"Error: {partition_data['error']}")
            return
        
        if partition_data['totalChunks'] == 0:
            print("Error en el cálculo del particionamiento.")
            return
        
        total_chunks = sum(len(chunks) for chunks in partition_data['chunkDistribution'].items())
        chunk_size = int(partition_data['chunkSize'] * 1_000_000)

        with open(file_name, "rb") as file:
            for data_node, chunk_array in partition_data['chunkDistribution'].items():
                for chunk in chunk_array:
                    print(f"Enviando Chunk {chunk} de {total_chunks} al nodo {data_node}...")
                    offset = (chunk - 1) * chunk_size
                    file.seek(offset)
                    data = file.read(chunk_size)
                    response = send_chunk(data_node, file_name, chunk, data)
                    print(f"Chunk {chunk} enviado, respuesta del servidor: {response}")

        response = await upload_success(file_name, partition_data['chunkSize'], partition_data['totalChunks'])
        print(response)
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo: {e}")

async def download_file(file_name: str):
    dir_name = f'{file_name}_chunks'
    download_data = await download_request(file_name)

    if 'error' in download_data:
        print(f"Error: {download_data['error']}")
        return
    

    chunks = download_data['chunks']
    totalChunks = download_data['totalChunks']

    for chunk, data_nodes in chunks.items():
        chunk_downloaded = False
        for data_node in data_nodes:
            print(f"Descargando Chunk {chunk} del nodo {data_node}...")
            chunk_downloaded = download_chunk(data_node, file_name, int(chunk))
            if chunk_downloaded:
                break
        if not chunk_downloaded:
            if os.path.exists(dir_name):
                shutil.rmtree(dir_name)
            print(f"Error al descargar el Chunk {chunk}.")
            return

    count = 1
    while os.path.exists(file_name):
        file_name = file_name.split('.')[0]+f'({count}).'+file_name.split('.')[1]
        file_name = file_name.split('(')[0]+f'({count})'+file_name.split(')')[-1]
        count += 1
    
    with open(f"{file_name}", 'wb') as output_file:
        for i in range(1, totalChunks + 1):
            chunk_path = os.path.join(dir_name, str(i))
            with open(chunk_path, 'rb') as chunk_file:
                output_file.write(chunk_file.read())
            os.remove(chunk_path)

        if not os.listdir(dir_name):
            os.rmdir(dir_name)
    
    print("Archivo descargado y ensamblado exitosamente.")





async def main():
    print("Bienvenido al sistema de almacenamiento distribuido.")
    print("Por favor, seleccione una opción:")
    print("1. Subir un archivo")
    print("2. Descargar un archivo")

    option = input("Opción: ")

    while option not in ['1', '2']:
        print("Opción no válida.")

        option = input("Opción: ")

    file_name = input("Ingrese el nombre del archivo: ")

    if option == '1':
        await upload_file(file_name)
    elif option == '2':
        await download_file(file_name)


if __name__ == "__main__":
    # run()
    asyncio.run(main())

