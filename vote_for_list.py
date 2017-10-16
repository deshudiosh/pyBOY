list = [["Harmony in Motion", "Wall Covering: Contract", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10916", 538],
        ["Tauko Stool", "Seating: Residential/Stool","https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10268", 140],
        ["Hybrid Collection Mesh Pattern ", "Materials, Treatments and Surfaces","https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10760", 331],
        ["Drum Teen", "Seating: Residental/Accent","https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/8545", 425],
        ["Tauko Modular Table", "Furniture: Contract/Tables", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10104", 381],
        ["Tauko Modular Table", "Furniture: Education", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10262", 169],
        ["Harmony in Motion", "Wall Covering: Paper", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/9569", 87],
        ["Tapa", "Seating: Contract/Lounge", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10270", 279],
        ["River Snake", "Furniture: Outdoor", "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/7775", 225]]


test_list = [["nazwa", "categoria", "url", 1],
             ["nazwa2", "categoria2", "url2", 2]]

def get_project_list():
    return [{"name": e[0], "category": e[1], "url": e[2], "num_iter": e[3]} for e in list]


