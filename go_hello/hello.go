package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from Go %s", r.URL.Path[1:])
}

func main() {
    http.HandleFunc("/hello", handler)
    //http.ListenAndServe(":8080", nil)
    l, err := net.Listen("unix", "/tmp/go_hello.sock")
    if err != nil {
        fmt.Printf("%s\n", err)
    } else {
        err := http.Serve(l, nil)
    }
}
