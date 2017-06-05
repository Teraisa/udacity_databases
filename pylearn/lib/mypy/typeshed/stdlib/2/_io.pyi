from typing import Any, BinaryIO, IO, Iterable, Iterator, List, Optional, Type, Tuple, Union

DEFAULT_BUFFER_SIZE = ...  # type: int


class BlockingIOError(IOError):
    characters_written = ...  # type: int

class UnsupportedOperation(ValueError, IOError): ...


class _IOBase(BinaryIO):
    def _checkClosed(self) -> None: ...
    def _checkReadable(self) -> None: ...
    def _checkSeekable(self) -> None: ...
    def _checkWritable(self) -> None: ...
    # All these methods are concrete here (you can instantiate this)
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> bytes: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> bytes: ...
    def readlines(self, hint: int = ...) -> list[bytes]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: Optional[int] = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: bytes) -> int: ...
    def writelines(self, lines: Iterable[bytes]) -> None: ...
    def next(self) -> bytes: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def __enter__(self) -> '_IOBase': ...
    def __exit__(self, t: Optional[Type[BaseException]], value: Optional[BaseException],
                 # TODO: traceback should be TracebackType but that's defined in types
                 traceback: Optional[Any]) -> bool: ...

class _BufferedIOBase(_IOBase):
    def read1(self, n: int) -> str: ...
    def read(self, n: int = ...) -> str: ...
    def readinto(self, buffer: bytearray) -> int: ...
    def write(self, s: str) -> int: ...
    def detach(self) -> "_BufferedIOBase": ...

class BufferedRWPair(_BufferedIOBase):
    def peek(self, n: int = ...) -> str: ...

class BufferedRandom(_BufferedIOBase):
    name = ...  # type: str
    raw = ...  # type: _IOBase
    mode = ...  # type: str
    def peek(self, n: int = ...) -> str: ...

class BufferedReader(_BufferedIOBase):
    name = ...  # type: str
    raw = ...  # type: _IOBase
    mode = ...  # type: str
    def peek(self, n: int = ...) -> str: ...

class BufferedWriter(_BufferedIOBase):
    name = ...  # type: str
    raw = ...  # type: _IOBase
    mode = ...  # type: str

class BytesIO(_BufferedIOBase):
    def __setstate__(self, tuple) -> None: ...
    def __getstate__(self) -> tuple: ...
    def getvalue(self) -> str: ...

class _RawIOBase(_IOBase):
    def readall(self) -> str: ...
    def read(self, n: int = ...) -> str: ...

class FileIO(_RawIOBase):
    mode = ...  # type: str
    closefd = ...  # type: bool
    def readinto(self, buffer: bytearray)-> int: ...
    def write(self, pbuf: str) -> int: ...

class IncrementalNewlineDecoder(object):
    newlines = ...  # type: Union[str, unicode]
    def decode(self, input, final) -> Any: ...
    def getstate(self) -> Tuple[Any, int]: ...
    def setstate(self, state: Tuple[Any, int]) -> None: ...
    def reset(self) -> None: ...

class _TextIOBase(_IOBase):
    errors = ...  # type: Optional[str]
    newlines = ...  # type: Union[str, unicode]
    encoding = ...  # type: Optional[str]
    def read(self, n: int = ...) -> str: ...
    def detach(self) -> None:
        raise UnsupportedOperation

class StringIO(_TextIOBase):
    line_buffering = ...  # type: bool
    def getvalue(self) -> str: ...
    def __setstate__(self, state: tuple) -> None: ...
    def __getstate__(self) -> tuple: ...

class TextIOWrapper(_TextIOBase):
    name = ...  # type: str
    line_buffering = ...  # type: bool
    buffer = ...  # type: str
    _CHUNK_SIZE = ...  # type: int

def open(file: Union[int, str], mode: str = ...) -> _IOBase: ...