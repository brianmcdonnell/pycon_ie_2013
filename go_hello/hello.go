package main

import (
    "os"
    "os/signal"
    "syscall"
    "fmt"
    "net"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    //fmt.Fprintf(w, "Hello from Go %s", r.URL.Path[1:])
    fmt.Fprintf(w, "Hello from Go")
}


func main() {
    http.HandleFunc("/hello", handler)
    //http.ListenAndServe(":8080", nil)
    l, err := net.Listen("unix", "/tmp/go_hello.sock")
    if err != nil {
        fmt.Printf("%s\n", err)
        os.Exit(0)
    }

    // Handle common process-killing signals so we can gracefully shut down:
    sigc := make(chan os.Signal, 1)
    signal.Notify(sigc, os.Interrupt, os.Kill, syscall.SIGTERM)
    go func(c chan os.Signal) {
        // Wait for a SIGINT or SIGKILL:
        sig := <-c
        fmt.Printf("Caught signal %s: shutting down.", sig)
        // Stop listening (and unlink the socket if unix type):
        l.Close()
        // And we're done:
        os.Exit(0)
    }(sigc)

    http.Serve(l, nil)
}
