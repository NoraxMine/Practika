from diag import Diag

if __name__ == "__main__":
    file_path = "states.csv"  # путь к CSV
    diagram = Diag(file_path)
    diagram.load_data()
    diagram.normal_bar()
