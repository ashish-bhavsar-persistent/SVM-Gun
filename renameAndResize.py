import os
from tqdm import tqdm

# Function to rename multiple files
def main():
    i = 1900
    for file_type in ['train/negative','train/positive_rest','test/negative','test/positive']:
        for im in tqdm(os.listdir(file_type)):
            imagePath = os.path.join(file_type, im)
            if "jpg" in imagePath:
                # print(imagePath)
                dst = str(i) + ".jpg"
                src = imagePath
                dst = os.path.join(file_type, dst)
                # print(dst)
                os.rename(src, dst)
                i += 1


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()