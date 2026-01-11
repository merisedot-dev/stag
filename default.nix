{
  pkgs,
  stdenv,
  python3Packages,
  merise_dot,
  ...
}:

let
  # version buffer variable
  stag_version = "0.1.0";
in
stdenv.mkDerivation {
  name = "stag";
  version = stag_version;

  # source file positions
  src = ./.;

  nativeBuildInputs = with pkgs; [
    meson # primary
    cmake # required by meson
    ninja # required by meson
    pkg-config # required by meson
    # languages (because meson is kinda stupid)
    python3
    # extra
    desktop-file-utils
  ];

  buildInputs = [ merise_dot ];

  propagatedBuildInputs =
    with pkgs;
    with python3Packages;
    [
      pygobject3
      gtk4
      libadwaita
    ];
}
