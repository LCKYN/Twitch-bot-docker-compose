import aiofiles


async def read_file(file_path):
    try:
        async with aiofiles.open(file_path, mode="rb") as file:
            data = await file.read()

            # When reading a csv file.
            # Return a dictionary of first column as key and second column as value.
            if file_path.endswith(".csv"):
                data = data.decode().split("\n")
                data = [line.split(",") for line in data]
                data = {line[0]: line[1] for line in data if line[0]}
                return data

            raise NotImplementedError("??")

    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred while reading the pickle file: {e}")
        return None


async def write_file(data, file_path):
    raise NotImplementedError("write_file")
    # try:
    #     async with aiofiles.open(file_path, mode="wb") as file:
    #         await file.write(pickle.dumps(data))
    # except Exception as e:
    #     print(f"An error occurred while writing the pickle file: {e}")
