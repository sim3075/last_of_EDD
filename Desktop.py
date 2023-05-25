from Folder import *
from File import *

class Desktop:
    def __init__(self,):
        self.root = Folder("root")
        self.types = {}
    
    def search_node(self, root, node):
        if root is None:
            return None
        
        if root.name == node:
            return root
        
        if isinstance(root, Folder):
            node_l = self.search_node(root.l_child, node)
            if node_l is not None:
                return node_l
            
            node_l_central = self.search_node(root.l_central_child, node)
            if node_l_central is not None:
                return node_l_central
            
            node_r_central = self.search_node(root.r_central_child, node)
            if node_r_central is not None:
                return node_r_central

            node_r = self.search_node(root.r_child, node)
            if node_r is not None:
                return node_r
            return None
    
    def search_father(self, root, node):
        if root is None or root.name == node:
            return None
        if isinstance(root, Folder):
            if root.l_child is not None and root.l_child.name == node:
                return root

            if root.l_central_child is not None and root.l_central_child.name == node:
                return root

            if root.r_central_child is not None and root.r_central_child.name == node:
                return root

            if root.r_child is not None and root.r_child.name == node:
                return root

            node_l = self.search_father(root.l_child, node)
            if node_l is not None:
                return node_l

            node_l_central = self.search_father(root.l_central_child, node)
            if node_l_central is not None:
                return node_l_central

            node_r_central = self.search_father(root.r_central_child, node)
            if node_r_central is not None:
                return node_r_central

            node_r = self.search_father(root.r_child, node)
            if node_r is not None:
                return node_r

            return None

   
    
    def insert_folder(self, parent, name_folder):
        new_folder = Folder(name_folder)
        parent_node = self.search_node(self.root, parent)
        if parent_node:
            if isinstance(parent_node, Folder):
                if parent_node.l_child is None:
                    parent_node.l_child = new_folder
                    return
                elif parent_node.l_central_child is None:
                    if parent_node.l_child.name != name_folder:
                        parent_node.l_central_child = new_folder
                        return
                    else:
                        print("Ya existe una carpeta con este nombre")
                elif parent_node.r_central_child is None:
                    if parent_node.l_child.name != name_folder and parent_node.l_central_child.name != name_folder:
                        parent_node.r_central_child = new_folder
                        return
                    else:
                        print("Ya existe una carpeta con este nombre")
                elif parent_node.r_child is None:
                    if parent_node.l_child.name != name_folder and parent_node.l_central_child.name != name_folder and parent_node.r_central_child.name != name_folder:
                        parent_node.r_child = new_folder
                        return
                    else:
                        print("Ya existe una carpeta con este nombre")
                else:
                    print("Carpeta llena")
            else:
                print("No puedes insertar carpetas en archivos")
        else:
            print("No se encotro esa carpeta")
    
    def insert_file(self, parent, name_file, extension_file, weight_file):
        new_file  = File(name_file, extension_file, weight_file)
        parent_node = self.search_node(self.root, parent)
        if parent_node:
            if isinstance(parent_node, Folder):
                if parent_node.l_child is None:
                    parent_node.l_child = new_file
                    return
                elif parent_node.l_central_child is None:
                    if parent_node.l_child.name != name_file:
                        parent_node.l_central_child = new_file
                        return
                    else:
                        print("Ya existe una archivo con este nombre")
                elif parent_node.r_central_child is None:
                    if parent_node.l_child.name != name_file and parent_node.l_central_child.name != name_file:
                        parent_node.r_central_child = new_file
                        return
                    else:
                        print("Ya existe una archivo con este nombre")
                elif parent_node.r_child is None:
                    if parent_node.l_child.name != name_file and parent_node.l_central_child.name != name_file and parent_node.r_central_child.name != name_file:
                        parent_node.r_child = new_file
                        return
                    else:
                        print("Ya existe una archivo con este nombre")
                else:
                    print("Carpeta llena")
            else:
                print("No puedes insertar archivos en archivos")
        else:
            print("No se encotro esa carpeta")

    def modify_folder(self, new_name, old_name):
        folder = self.search_node(self.root, old_name)
        parent_node = self.search_father(self.root, old_name)
        if folder:
            elements = [parent_node.l_child, parent_node.l_central_child, parent_node.r_central_child, parent_node.r_child]
            if folder is None:
                print("No se encontro esta carpeta")
                return
            if [element for element in elements if element and element.name == new_name]:
                print("Ya existe un elemento con ese nombre")
                return
            folder.modify_name(new_name)
        else:
            print("No se encontro la carpeta")
    
    def modify_file(self, old_name, new_name, new_extension, new_weight):
        file_node = self.search_node(self.root, old_name)
        parent_file = self.search_father(self.root, old_name)
        if file_node:
            elements = [parent_file.l_child, parent_file.l_central_child, parent_file.r_central_child, parent_file.r_child]
            if file_node is None:
                print("No se encontro esta carpeta")
                return
            if [element for element in elements if element and element.name == new_name]:
                print("Ya existe un elemento con ese nombre")
                return
            file_node.modify_name(new_name)
            file_node.modify_extension(new_extension)
            file_node.modify_weight(new_weight)
        else:
            print("No se encontro la carpeta")

    def is_type(self, root):
        if root is None:
            return None
        else:
            if isinstance(root, File):
                if root.extension in self.types.keys():
                    self.types[root.extension] = self.types.get(root.extension+1)
                if root.extension not in self.types.keys():
                    self.types.setdefault(root.extension, 1)

            else:
                self.is_type(root.l_child)
                self.is_type(root.l_central_child)
                self.is_type(root.r_central_child)
                self.is_type(root.r_child)


    

    def imprimir_arbol(self):
        self.imprimir_subarbol(self.root, 0)

    def imprimir_subarbol(self, nodo_actual, nivel):
        print(" " * nivel, end="")
        if isinstance(nodo_actual, File):
            print("- " + nodo_actual.filename())
        if isinstance(nodo_actual, Folder):
            print("- " + nodo_actual.name)
            if nodo_actual.l_child is not None:
                self.imprimir_subarbol(nodo_actual.l_child, nivel + 2)
            if nodo_actual.l_central_child is not None:
                self.imprimir_subarbol(nodo_actual.l_central_child, nivel + 2)
            if nodo_actual.r_central_child is not None:
                self.imprimir_subarbol(nodo_actual.r_central_child, nivel + 2)
            if nodo_actual.r_child is not None:
                self.imprimir_subarbol(nodo_actual.r_child, nivel + 2)

            
                

