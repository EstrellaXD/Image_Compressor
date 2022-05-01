from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
import os
import cv2
import tkinter as tk
from tkinter import filedialog
import argparse
import time
import math


def is_image(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])


def get_path():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    try:
        image_filenames = [os.path.join(folder_path, x) for x in os.listdir(folder_path) if is_image(x)]
    except:
        print('error')
        quit()
    else:
        return image_filenames


def cv2_improcess(file_path):
    fpath = os.path.join(file_path)
    image = cv2.imread(fpath)
    h, w, c = image.shape
    c_times = math.sqrt(args.number)
    c_w = int(w/c_times)
    c_h = int(h/c_times)
    resized_img = cv2.resize(image, (c_w, c_h))
    cv2.imwrite(file_path, resized_img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='compressor time')
    parser.add_argument('--number', '-n', help='compressor time, default is 2', default=2)
    args = parser.parse_args()
    image_path = get_path()
    start_time = time.time()
    pool_size = cpu_count()
    pool = ThreadPool(pool_size)
    pool.map(cv2_improcess, image_path)
    pool.close()
    pool.join()
    end_time = time.time()
    print('finished, use {} s'.format(end_time-start_time))
