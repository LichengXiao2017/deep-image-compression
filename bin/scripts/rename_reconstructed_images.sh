for image in ../data/test/reconstructed/balle2018/*
do
  mv ${image} ${image//png.tfci.png/png}
done
