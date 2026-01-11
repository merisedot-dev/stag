{
  description = "Stag frontend environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
    # the custom library
    mdot = {
      url = "github:merisedot-dev/merise_dot";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      mdot,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        merise_dot = mdot.packages."${system}".default;
      in
      {
        packages.default = pkgs.callPackage ./default.nix { inherit merise_dot; };

        devShells.default = pkgs.mkShell {
          name = "stagshell";
          inputsFrom = [ self.packages."${system}".default ];
          packages = with pkgs; [ just ];
        };
      }
    );
}
