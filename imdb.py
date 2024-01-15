class InMemoryDatabase:
    def __init__(self):
        self.data = {}
        self.transactions = []
        self.transaction_pointer = -1

    def set(self, name, value):
        self.data[name] = value
        print(f"SET {name} => {value}")

    def get(self, name):
        value = self.data.get(name, "NULL")
        print(f"GET {name} => {value}")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"DELETE {name}")
        else:
            print(f"Name not found: {name}")

    def count(self, value):
        count = list(self.data.values()).count(value)
        print(f"COUNT {value} => {count}")

    def begin(self):
        self.transaction_pointer += 1
        self.transactions.append(dict(self.data))
        print("BEGIN")

    def rollback(self):
        if self.transaction_pointer >= 0:
            self.data = dict(self.transactions[self.transaction_pointer])
            self.transactions.pop()
            self.transaction_pointer -= 1
            print("ROLLBACK")
        else:
            print("TRANSACTION NOT FOUND")

    def commit(self):
        self.transactions = []
        self.transaction_pointer = -1
        print("COMMIT")

    def end(self):
        print("END")
        exit()

def main():
    db = InMemoryDatabase()

    while True:
        try:
            user_input = input().split()
            command = user_input[0]

            if command == "SET":
                db.set(user_input[1], user_input[2])
            elif command == "GET":
                db.get(user_input[1])
            elif command == "DELETE":
                db.delete(user_input[1])
            elif command == "COUNT":
                db.count(user_input[1])
            elif command == "BEGIN":
                db.begin()
            elif command == "ROLLBACK":
                db.rollback()
            elif command == "COMMIT":
                db.commit()
            elif command == "END":
                db.end()
            else:
                print("Invalid command")

        except IndexError:
            print("Invalid input. Please provide the correct number of arguments.")
        except KeyboardInterrupt:
            print("\nExiting the database.")
            break

if __name__ == "__main__":
    main()
