# Fonction pour parcourir les éléments du DOM
def traverse_dom(element, level=0):
    # Afficher l'élément actuel
    if element.name:
        print(f"{' ' * level}<{element.name}>")

    # Si l'élément a des enfants
    if hasattr(element, 'children'):
        for child in element.children:
            traverse_dom(child, level + 1)
