package lib

import "log"

func CheckError(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
