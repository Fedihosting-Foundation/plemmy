from io import TextIOWrapper

File = tuple[str | None, bytes | str | TextIOWrapper]
UploadFile = dict[str, File]
