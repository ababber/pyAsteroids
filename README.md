# [pyAsteroids](./pyAsteroids.mov)

## depends on `macOS`/`linux`, `python >= 3.7`, `pygame`, `bash`/`zsh`

* `pip install -r requirements.txt` for python requirements before running

## running

* `python main.py`

## game play controls

* `w`: move forward
* `s`: move backward
* `d`: rotate clockwise
* `a`: rotate counter clockwise
* `space`: shoot bullet

## description

* A `boot.dev` guided project
  * everything after commit id `9c6f183c2817b3a0e835843487c3cc32580e0380` are features added beyond scope of project.
* features added beyond scope of project:
  * currently using `pyenv` and `pyenv-virtualenv` instead of `venv` for development

## to do

* [ ] fix: edge case of player moving off screen
* [ ] fix: crashes after a few minutes of gameplay
* [ ] add intro and outro title screen
* [ ] add asteroid to asteroid collision feature, currently asteroids overlap instead of collide
* [ ] add levels, next level acheived by destroying `x` asteroids per level and advancing displays next level title screen
* [ ] add stats
* [ ] add AI boss level

## refs

* [pygame docs](https://www.pygame.org/docs/ref/pygame.html)
* [unit vector](https://en.wikipedia.org/wiki/Unit_vector)
* [collision detection](https://en.wikipedia.org/wiki/Collision_detection)
