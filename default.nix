{
  pkgs,
  stdenv,
  python3Packages,
  ...
}:

let
  # version buffer variable
  stag_version = "0.1.0";
in
stdenv.mkDerivation {
  name = "stag";
  version = stag_version;

  src = ./.;

  nativeBuildInputs = with pkgs; [
    # build toolkits
    meson
    cmake
    ninja
    pkg-config
    # languages (because)
    python3
    # extra
    desktop-file-utils
  ];

  propagatedBuildInputs =
    with pkgs;
    with python3Packages;
    [
      pygobject3
      gtk4
      libadwaita
    ];
}
