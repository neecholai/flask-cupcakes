$(function () {

  async function getCupcakes() {
    let response = await axios.get('/api/cupcakes');

    return response.data.cupcakes;
  }

  function showCupcakes(cupcakes) {

    for (let cupcake of cupcakes) {
      let flavor = cupcake.flavor;
      let size = cupcake.size;
      let rating = cupcake.rating;
      let image = cupcake.image;

      // let newCupcake = `<div>${image}</li>`

      // $('<img>').attr(src, image)
    }
  }

  function initializeHomepage() {
    let cupcakeList = getCupcakes();

    showCupcakes(cupcakeList);
  }

})