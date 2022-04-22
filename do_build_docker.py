#!/usr/bin/env python
import os
import subprocess


THIS_DIR = os.path.realpath(os.path.dirname(__file__))
DOCKER_IMAGE_NAME = "test_conan_opencv_codecs_image"
DOCKER_CONTAINER_NAME = "test_conan_opencv_codecs"


def run(cmd):
    print(f"\n****** {cmd} ******")
    out = subprocess.check_output(cmd, shell=True).decode("utf-8")
    print(out)
    print()
    return out


def run_follow_log(cmd):
    print(f"\n****** {cmd} ******")
    subprocess.check_call(cmd, shell=True)


def main():

    run(f"docker build -t {DOCKER_IMAGE_NAME} .")

    active_containers = run("docker ps -a").split("\n")
    need_start_container = len(list(filter(lambda s: DOCKER_CONTAINER_NAME in s, active_containers))) == 0

    print(f"{need_start_container=}")
    if need_start_container:
        run(f"docker run --name {DOCKER_CONTAINER_NAME} -it -d -v $(pwd):/sources {DOCKER_IMAGE_NAME} /bin/bash")

    run(f"docker start {DOCKER_CONTAINER_NAME}")
    run_follow_log(f"docker exec -it {DOCKER_CONTAINER_NAME} /sources/do_build.sh")

    print(f"""
    Once you are finished, remove the container and image with
    
    docker stop {DOCKER_CONTAINER_NAME} && docker rm {DOCKER_CONTAINER_NAME}
    docker rmi {DOCKER_IMAGE_NAME}
    """)


if __name__ == "__main__":
    main()
