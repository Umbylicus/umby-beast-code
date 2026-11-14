# Folder layouts

`game_scaffold.py init` creates these. Keep to them. A file with no obvious home means a missing folder in the design, so add the folder on purpose and note it in `docs/design.md`.

Shared by every engine:

```
assets/manifest.json   every asset: id, file, type, license, source, author, generated
CREDITS.md             human-readable credits, kept in step with the manifest
LICENSES/              full license text for each third-party pack or font
docs/game-plan.md      AGREED plan the build follows (engine, loop, scope, skills)
docs/design.md         short notes; the plan file is the source of truth
docs/balance.md        difficulty curve and tuning notes
tests/                 logic tests and the browser smoke test
scripts/               asset packing, manifest and build helpers
.beast/                 critic rounds, evidence, score graph, work log
```

## Browser 2D (Phaser or PixiJS, TypeScript, Vite)

```
index.html
src/
  main.ts          bootstrap only
  config/          tuning values, input bindings, palette
  scenes/          boot, preload, menu, game, ui, game-over
  entities/        one file per entity: player, enemy, pickup
  systems/         spawning, collision, scoring, camera, feedback, save
  ui/              display, menus, shared buttons
  level/           level data loaders, tilemap helpers
  utils/           math, seeded random, timers
  types/           shared types
assets/
  src-art/         layered source files, never shipped
  sprites/         exported images, one folder per entity
  atlases/         packed sheets and their data files (generated)
  tilesets/        tile images and map files
  audio/sfx/       short effects
  audio/music/     loops
  fonts/           web fonts, each with its license beside it
  shaders/
  data/            level and balance data
dist/              build output, ignored by git
```

## Browser 3D (Three.js or Babylon, TypeScript, Vite)

```
index.html
src/
  main.ts          bootstrap, renderer, loop
  core/            fixed-step loop, input, time, events
  scenes/          world and level setup, menus
  entities/        one module per entity: mesh, logic, state
  systems/         physics or collision, camera rig, audio, feedback, spawning, save
  render/          materials, shader loading, post-processing, lighting
  loaders/         asset loading with progress, model and texture decoders
  ui/              display and menus
  data/            balance and level config
public/
  models/          runtime models, compressed
  textures/        runtime textures
  audio/sfx/  audio/music/
assets/
  src-art/         modelling and texturing source files, never served
dist/
```

Dispose of geometry, materials, and textures when a scene unloads.

## Godot 4

Godot's own guidance is to keep a scene's assets beside the scene and use `snake_case` for files and folders.

```
project.godot
addons/            third-party plugins only, each with its license
scenes/
  main/            main scene and script
  player/          scene, script, and the sprites and sounds only it uses
  enemies/
  levels/          one folder per level
  ui/
scripts/           autoloads and shared utilities
systems/           spawning, feedback, save, random
resources/         data resources: balance, items, cards
assets/            shared assets no single scene owns
  sprites/ tilesets/ fonts/ shaders/ audio/sfx/ audio/music/ models/
  src-art/         source files, with an empty .gdignore so Godot skips them
docs/              with an empty .gdignore
build/             exports, ignored by git
```

PixiJS and plain canvas use the Browser 2D layout. Babylon uses the Browser 3D layout.

## Unity

```
Assets/
  Scripts/Core  Entities  Systems  UI
  Scenes/
  Prefabs/
  Art/Sprites  Art/Audio/Sfx  Art/Audio/Music
ProjectSettings/
Packages/
docs/              game-plan.md lives here; Unity ignores it if you add a .meta as needed
```

## React Native

```
src/game  src/entities  src/systems  src/ui  src/config
assets/sprites  assets/audio/sfx  assets/audio/music
docs/
```
