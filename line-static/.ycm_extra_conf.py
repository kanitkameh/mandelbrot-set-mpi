def Settings( **kwargs ):
  return {
    'flags': [ 'clang++', '-I/opt/homebrew/Cellar/open-mpi/4.1.5/include', '-L/opt/homebrew/Cellar/open-mpi/4.1.5/lib', '-L/opt/homebrew/opt/libevent/lib', '-lmpi' ],
  }
