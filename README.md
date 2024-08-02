# Development Notes

This worked to compile (I originally ran it when the files were all in the directory root):

`python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. measurement.proto`

To import into your project:
`pip install -m git+https://github.com/SirenOpt/lib_plasmasens_protobuf.git`
