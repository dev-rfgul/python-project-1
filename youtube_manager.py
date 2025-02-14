import json 

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(videos):
    with open("youtube.txt", 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    print("\n" + "="*50)
    print("📺  YOUTUBE VIDEO LIST  📺".center(50))
    print("="*50)

    if not videos:
        print("\n⚠️  No videos found.\n")
        return

    for index, video in enumerate(videos, start=1):
        print(f" {index}. {video['name']} - {video['time']}")
        print("-" * 50)

def add_a_video(videos):
    print("\n➕ ADD A VIDEO ➕")
    name = input("Enter video name: ").strip()
    time = input("Enter video time: ").strip()

    videos.append({"name": name, "time": time})
    save_data(videos)

    print("\n✅ Video added successfully!\n")

def update_a_video(videos):
    list_all_videos(videos)
    
    print("\n✏️  UPDATE A VIDEO ✏️")
    try:
        index = int(input("Enter video number to update: ")) - 1
        if 0 <= index < len(videos):
            videos[index]["name"] = input("Enter new video name: ").strip() or videos[index]["name"]
            videos[index]["time"] = input("Enter new video time: ").strip() or videos[index]["time"]
            save_data(videos)
            print("\n✅ Video updated successfully!\n")
        else:
            print("\n⚠️  Invalid video number.\n")
    except ValueError:
        print("\n⚠️  Invalid input. Please enter a number.\n")

def delete_a_video(videos):
    list_all_videos(videos)
    
    print("\n🗑️  DELETE A VIDEO 🗑️")
    try:
        index = int(input("Enter video number to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted_video = videos.pop(index)
            save_data(videos)
            print(f"\n✅ Deleted: {deleted_video['name']}\n")
        else:
            print("\n⚠️  Invalid video number.\n")
    except ValueError:
        print("\n⚠️  Invalid input. Please enter a number.\n")

def main():
    videos = load_data()
    
    while True:
        print("\n" + "="*50)
        print("🎬  YOUTUBE MANAGER  🎬".center(50))
        print("="*50)
        print("1️⃣  List all YouTube videos")
        print("2️⃣  Add a YouTube video")
        print("3️⃣  Update a YouTube video")
        print("4️⃣  Delete a YouTube video")
        print("5️⃣  Exit")
        print("="*50)

        choice = input("\nEnter your choice: ").strip()
        
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
                print("\n👋 Goodbye!\n")
                break
            case _:
                print("\n⚠️  Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
