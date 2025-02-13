import json 

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
            # print(type(test))
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(videos):
    with open("youtube.txt", 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    if not videos:
        print("No videos found.")
    print("\n")
    print("* "*40)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - {video['time']}")
        print("\n")
    print("* "*30)
def add_a_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data(videos)
    print("Video added successfully.")

def update_a_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter video number to update: ")) - 1
        if 0 <= index < len(videos):
            videos[index]["name"] = input("Enter new video name: ")
            videos[index]["time"] = input("Enter new video time: ")
            save_data(videos)
            print("Video updated successfully.")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Invalid input.")

def delete_a_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter video number to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted_video = videos.pop(index)
            save_data(videos)
            print(f"Deleted: {deleted_video['name']}")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Invalid input.")

videos = load_data()

def main():
    while True:
        print("\nYoutube Manager || Main Menu")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")
        
        choice = input("Enter your choice: ") 
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_a_video(videos)
            case '3':
                update_a_video(videos)
            case '4':
                delete_a_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
