from app.plant_identifier import identify_plant
from app.health_recommender import get_remedy

def main():
    print("1. Identify Plant from Image")
    print("2. Get Health Remedy for Disease")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        img_path = input("Enter image path: ")
        plant, benefits = identify_plant(img_path)
        print(f"\nPlant Identified: {plant}")
        print("Benefits:")
        for i, benefit in enumerate(benefits, 1):
            print(f"{i}. {benefit}")
    elif choice == '2':
        disease = input("Enter disease name: ")
        get_remedy(disease)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()