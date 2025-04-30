package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	conn, err := net.Dial("tcp", "127.0.0.1:5000")
	if err != nil {
		fmt.Println("Lỗi kết nối:", err)
		return
	}
	defer conn.Close()

	fmt.Println("Đã kết nối tới server.")

	go func() {
		reader := bufio.NewReader(conn)
		for {
			msg, err := reader.ReadString('\n')
			if err != nil {
				fmt.Println("Server đóng kết nối.")
				os.Exit(0)
			}
			fmt.Print("Another_User:", msg)
		}
	}()

	// Gửi dữ liệu từ bàn phím
	inputReader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print("You: ")
		text, _ := inputReader.ReadString('\n')
		_, err := conn.Write([]byte(text))
		if err != nil {
			fmt.Println("Lỗi gửi:", err)
			break
		}
	}
}
