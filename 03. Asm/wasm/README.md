### EMSDK  
`install https://emscripten.org/docs/getting_started/downloads.html`  

### C to WASM  
`emcc counter.c -s WASM=1 -s SIDE_MODULE=1 -o counter.wasm`  
