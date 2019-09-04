import imdir
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", required=True,
                    help="path of directory",)
parser.add_argument("-n", "--nthreads", default=-1, type=int,
                    help="number of threads")
parser.add_argument("-r", "--recursive", type=bool, default=False,
                    help="whether to recurively traverse the sub directories")
args = parser.parse_args()
start = time.time()
im_dir = imdir.image_dir(args.path, args.recursive, args.nthreads)
print("time taken: {} number of images: {}".format(
    time.time() - start, len(im_dir.file_list)))
