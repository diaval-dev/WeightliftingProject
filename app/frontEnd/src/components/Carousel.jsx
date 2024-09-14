import picture1 from "../assets/img/foto_carrusel_1.png";
import picture2 from "../assets/img/foto_carrusel_2.jpg";

export default function Carousel() {
  return (
    <section class="container-fluid p-0">
      <div id="blog-carousel" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img class="w-100" src={picture1} alt="Image" />
            <div class="carousel-caption d-flex flex-column align-items-center justify-content-center">
              <h3 class="text-primary text-capitalize m-0">
                Liga De Levantamiento Olimpico Del Cauca
              </h3>
              <h2 class="display-2 m-0 mt-2 mt-md-4 text-white font-weight-bold text-capitalize">
                Preparate para competir!
              </h2>
              <a
                href=""
                class="btn btn-lg btn-outline-light mt-3 mt-md-5 py-md-3 px-md-5"
              >
                Registro Deportistas
              </a>
            </div>
          </div>
          <div class="carousel-item">
            <img class="w-100" src={picture2} alt="Image" />
            <div class="carousel-caption d-flex flex-column align-items-center justify-content-center">
              <h3 class="text-primary text-capitalize m-0">
                Liga De Levantamiento Olimpico Del Cauca
              </h3>
              <h2 class="display-2 m-0 mt-2 mt-md-4 text-white font-weight-bold text-capitalize">
                Preparate para competir!
              </h2>
              <a
                href=""
                class="btn btn-lg btn-outline-light mt-3 mt-md-5 py-md-3 px-md-5"
              >
                Registro Deportistas
              </a>
            </div>
          </div>
        </div>
        <a
          class="carousel-control-prev"
          href="#blog-carousel"
          data-slide="prev"
        >
          <span class="carousel-control-prev-icon"></span>
        </a>
        <a
          class="carousel-control-next"
          href="#blog-carousel"
          data-slide="next"
        >
          <span class="carousel-control-next-icon"></span>
        </a>
      </div>
    </section>
  );
}
