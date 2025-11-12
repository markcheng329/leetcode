// Last updated: 11/12/2025, 4:56:47 AM
function createHelloWorld(){
    return function(...args){
        return "Hello World"
    }
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */