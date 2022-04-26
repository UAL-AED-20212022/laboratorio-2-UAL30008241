from models.LinkedList import LinkedList



def main():
    lista_ligada = LinkedList()
    while True:
        try:
            comandos = input().split(" ")
        except EOFError:
            return
        match comandos[0]:
            case "RPI":
                lista_ligada.insert_at_start(comandos[1])
                lista_ligada.traverse_list()
            case "RPF":
                lista_ligada.insert_at_end(comandos[1])
                lista_ligada.traverse_list()
            case "RPDE":
                lista_ligada.insert_after_item(comandos[2],comandos[1])
                lista_ligada.traverse_list()
            case "RPAE":
                lista_ligada.insert_before_item(comandos[2],comandos[1])
                lista_ligada.traverse_list()
            case "RPII":
                lista_ligada.insert_at_index(int(comandos[2]), comandos[1])
                lista_ligada.traverse_list()
            case "VNE":
                print(f"O número de elementos são {lista_ligada.get_count()}.")
            case "VP":
                if lista_ligada.search_item(comandos[1]) == True:
                    print(f"O país {comandos[1]} encontra-se na lista.")
                else:
                    print(f"O país {comandos[1]} não se encontra na lista.")
            case "EPE":
                print(f"O país {lista_ligada.start_node.get_item()} foi eliminado da lista.")
                lista_ligada.delete_at_start()
            case "EUE":
                print(f"O país {lista_ligada.get_last_node()} foi eliminado da lista.")
                lista_ligada.delete_at_end()
            case "EP":
                if lista_ligada.search_item(comandos[1]) == False:
                    print(f"O país {comandos[1]} não se encontra na lista.")
                else:    
                    lista_ligada.delete_element_by_value(comandos[1])
                    print(f"O país {comandos[1]} foi eliminado da lista.")
            case "":
                break
            case default:
                pass