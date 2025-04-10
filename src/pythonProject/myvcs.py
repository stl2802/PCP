import argparse
import os

REPO_DIR = ".myvcs"
version = "1.0"  # потом изменим

def main():
#crete and replase file
    def crete_GitPlach():
        if (os.path.isdir(".GitPlach") == False):
            os.mkdir(r".GitPlach")
            os.chdir(r".GitPlach/")
            os.mkdir(r"objects")
            with open("index", "w") as areaindex:
                pass


    def add(filename):
        index_file = os.path.join(".GitPlach", "index.txt")

        if os.path.exists(".GitPlach"):
            try:
                with open(index_file, "r", encoding="utf-8") as index:
                    lines = index.readlines()

                with open(index_file, "w", encoding="utf-8") as index:
                    for line in lines:
                        index.write(line)
                    index.write(f"{filename}\n")

                print(f"Файл '{filename}' добавлен в индекс.")

            except FileNotFoundError:
                print("Файл index не найден.")
            except Exception as e:
                print(f"Ошибка при работе с файлом index: {e}")
        else:
            print("Директория .GitPlach не найдена.")



    def remove(filename):
        index_file = os.path.join(".GitPlach", "index.txt")

        if os.path.exists(".GitPlach"):
            try:
                with open(index_file, "r", encoding="utf-8") as index:
                    lines = index.readlines()

                new_lines = []
                delete_block = False

                for line in lines:
                    if line == f"{filename}\n":
                        delete_block = True
                    elif delete_block:
                        if line.strip() == "":
                            delete_block = False
                        continue
                    else:
                        new_lines.append(line)

                with open(index_file, "w", encoding="utf-8") as index:
                    index.writelines(new_lines)

                print(f"Блок строк, начинающийся с '{filename}', удален из индекса.")

            except FileNotFoundError:
                print("Файл index не найден.")
            except Exception as e:
                print(f"Ошибка при работе с файлом index: {e}")
        else:
            print("Директория .GitPlach не найдена.")

        def line(line_name):
            pass
        def check():
            pass

    def save(commit_name):
        gitplach_dir = ".GitPlach"
        index_file = os.path.join(gitplach_dir, "index.txt")

        if not os.path.exists(gitplach_dir):
            print(f"Директория '{gitplach_dir}' не найдена.")
            return

        object_dir = os.path.join(gitplach_dir, "objects")
        commit_file = os.path.join(object_dir, commit_name)

        try:
            with open(index_file, "r", encoding="utf-8") as index_file_read:
                lines = index_file_read.readlines()

            with open(commit_file, "w", encoding="utf-8") as commit_file_write:
                for line in lines:
                    commit_file_write.write(line)
            print("Успешно")

        except FileNotFoundError:
            print("Файл index не найден.")
        except Exception as e:
            print(f"Ошибка при работе с файлом index: {e}")

        def switch(line_name):
            pass

        def zatuchka():
            print("Затычка")


#cli
    parser = argparse.ArgumentParser(
        description="У давай поплачь что у тебя сного не замерджилось", prog="GitPlach"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")


    parser.add_argument(
        "--version",
        "--ver",
        action="version",
        version=f"GitPlach {version}",
        help="Show version number",
    )

    #init
    init_pareser = subparsers.add_parser("init", help="инициализировать репозиторий")
    #init_pareser.add_argument("patch_to_derectory", help="", required=False)

    #add
    add_parser = subparsers.add_parser("add", help="добавить файл к коммиту")
    add_parser.add_argument("patch_to_derectory", help="")
    #remove
    remove_parser = subparsers.add_parser("remove", help="удалить файл из коммита")
    remove_parser.add_argument("filename",help="название файла")
    #switch
    switch_parser = subparsers.add_parser("switch", help="переключиться на другую линию")
    #backto
    backto_parser = subparsers.add_parser("backto", help="вернуться на коммит [название коммита]")
    #save
    save_parser = subparsers.add_parser("save", help="сохранить")
    #check
    check_parser = subparsers.add_parser("check", help="посмотреть коммиты")
    #publish от это на потом
    publish_parser = subparsers.add_parser("publish", help="опубликовать на PlachHab")
    #line
    line_parser = subparsers.add_parser("line", help="линия")

    args = parser.parse_args()

    if args.command == "init":
        crete_GitPlach()
    elif args.command == "add":
        add(123)
    elif args.command == "remove":
        filename = args.filename
        remove(filename)
    elif args.command == "switch":
        pass
    elif args.command == "backto":
        pass
    elif args.command == "save":
        save("1")
    elif args.command == "check":
        pass
    elif args.command == "publish":
        pass
    elif args.command == "line":
        pass
#cli

if __name__ == "__main__":
    main()