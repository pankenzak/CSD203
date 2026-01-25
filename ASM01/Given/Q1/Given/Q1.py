# ========================HELPER FUNCTION (DO NOT EDIT)============================
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line = file.readline()
        return eval(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
# =================================================================================

class Song:
    def __init__(self, song_id=None, title=None, artist=None, duration=None):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"({self.song_id}, {self.title}, {self.artist}, {self.duration})"

class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class PlayNextQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def load_data(self, file_path, size):
        data = read_file(file_path)
        queue_data = data[0]
        for i in range(min(size, len(queue_data))):
            song_info = queue_data[i]
            self.helper_fn(Song(song_info[0], song_info[1], song_info[2], song_info[3]))

    def enqueue(self, song):
        # You should write here appropriate statements to complete this function.
        # --------------------------------------------------------
        self.helper_fn(song) #Su dung helper_fn co san va them vao rear
        # ---------------------------------------------------------

    def dequeue(self):
        # You should write here appropriate statements to complete this function.
        # --------------------------------------------------------
        pass
        # ---------------------------------------------------------
        
    def display(self):
        print("Play Next Queue:")
        if self.is_empty():
            print("Empty")
        else:
            current = self.front
            while current:
                print(current.info)
                current = current.next
        print("=========")
    
    def helper_fn(self, song):
        new_node = Node(song)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

class PlaylistCLL:
    def __init__(self):
        self.tail = None

    def is_empty(self):
        return self.tail is None

    def load_data(self, file_path, size):
        data = read_file(file_path)
        playlist_data = data[1]
        for i in range(min(size, len(playlist_data))):
            song_info = playlist_data[i]
            self.helper_fn(Song(song_info[0], song_info[1], song_info[2], song_info[3]))

    def add_to_playlist(self, song):
        # You should write here appropriate statements to complete this function.
        # --------------------------------------------------------
        self.helper_fn(song) #Su dung helper_fn co san va them vao cuoi
        # ---------------------------------------------------------

    def search_by_artist(self, artist_name):
        found_songs = []
        # You should write here appropriate statements to complete this function.
        # --------------------------------------------------------
        if self.is_empty():
            return found_songs 
        current = self.tail.next # con tro tai head
        while True : # tao vong lap vo han 
            if current.info.artist.strip().lower() == artist_name.strip().lower():# cho artist va artist_name deu in thuong de de so sanh
                found_songs.append(current.info)
            current = current.next 
            if current == self.tail.next:
                break
        pass
        # ---------------------------------------------------------
        return found_songs

    def remove_from_playlist(self, song_id):
        # You should write here appropriate statements to complete this function.
        # --------------------------------------------------------
        pass
        # ---------------------------------------------------------

    def reverse_playlist(self):
        # You should write here appropriate statements to complete this function.
        # --------------------------------------------------------
        pass
        # ---------------------------------------------------------

    def display(self):
        print("Playlist (CLL):")
        if self.is_empty():
            print("Empty")
        else:
            current = self.tail.next
            while True:
                print(current.info)
                current = current.next
                if current == self.tail.next:
                    break
        print("=========")
    
    def helper_fn(self, song):
        new_node = Node(song)
        if self.is_empty():
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node


class MusicPlayer:
    def __init__(self):
        self.play_next_queue = PlayNextQueue()
        self.playlist_cll = PlaylistCLL()

    def load(self, file_path, m):
        self.play_next_queue.load_data(file_path, m)
        self.playlist_cll.load_data(file_path, m)

    def display(self):
        self.play_next_queue.display()
        self.playlist_cll.display()

    def f1(self, artist_name):
        return self.playlist_cll.search_by_artist(artist_name)

    def f2(self, song_for_playlist, song_for_queue):
        self.playlist_cll.add_to_playlist(song_for_playlist)
        self.play_next_queue.enqueue(song_for_queue)

    def f3(self, song_id_to_remove):
        dequeued_song = self.play_next_queue.dequeue()
        self.playlist_cll.remove_from_playlist(song_id_to_remove)
        return dequeued_song

    def f4(self):
        self.playlist_cll.reverse_playlist()


# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    player = MusicPlayer()

    file_path = input("Please input file name (ex: data.txt):  ")

    initial_data = read_file(file_path)
    
    max_queue_size = len(initial_data[0])
    max_playlist_size = len(initial_data[1])
    max_size = max(max_queue_size, max_playlist_size)
    
    prompt = f"Input the data size (from 0 to {max_size}):\nm =   "
    m = int(input(prompt))
    while not (0 <= m <= max_size):
        m = int(input(f"Please input a size from 0 to {max_size}:\nm =   "))
    

    print("\nSelect a function to run:")
    print("1. Run f1() - Search by Artist")
    print("2. Run f2() - Add New Songs")
    print("3. Run f3() - Remove Songs")
    print("4. Run f4() - Reverse Playlist")
    n = int(input("Input a question (1-4): "))

    player.load(file_path, m)

    if n == 1:
        search_name = str(input("Enter Artist Name to search: "))
        print("\nOUTPUT:")
        print("State before searching:")
        player.display()
        found_songs = player.f1(search_name)
        print("Search Results:")
        if found_songs:
            for song in found_songs:
                print(song)
        else:
            print("No songs found for this artist.")

    elif n == 2:
        print("Enter new song details for the playlist:")
        p_id = input("  ID: ")
        p_title = input("  Title: ")
        p_artist = input("  Artist: ")
        p_duration = int(input("  Duration: "))
        song_p = Song(p_id, p_title, p_artist, p_duration)

        print("Enter new song details for the queue:")
        q_id = input("  ID: ")
        q_title = input("  Title: ")
        q_artist = input("  Artist: ")
        q_duration = int(input("  Duration: "))
        song_q = Song(q_id, q_title, q_artist, q_duration)

        print("\nOUTPUT:")
        print("--- Before Adding ---")
        player.display()
        player.f2(song_p, song_q)
        print("\n--- After Adding ---")
        player.display()

    elif n == 3:
        delete_song_id = str(input("Enter Song ID to remove from playlist: "))
        print("\nOUTPUT:")
        print("--- Before Removing ---")
        player.display()
        dequeued = player.f3(delete_song_id)
        print("\n--- After Removing ---")
        print(f"Dequeued Song: {dequeued}")
        player.display()
    
    elif n == 4:
        print("\nOUTPUT:")
        print("--- Before Reversing ---")
        player.display()
        player.f4()
        print("\n--- After Reversing ---")
        player.display()

    else:
        print("Invalid selection.")

# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ================================
