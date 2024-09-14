import teamColombia from "../../assets/img/team_colombia.jpg";

export default function AboutStart() {
  return (
    <section class="container py-5">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <img class="img-fluid mb-4 mb-lg-0" src={teamColombia} alt="Image" />
        </div>
        <div class="col-lg-6">
          <h2 class="display-4 font-weight-bold mb-4">Team Colombia</h2>
          <p>
            Presentamos a nuestros deportistas colombianos que nos representaron
            en levantamiento de pesas en los olimpicos de paris 2024
          </p>
          <div class="row py-2">
            <div class="col-sm-6">
              <i class="flaticon-barbell display-2 text-primary"></i>
              <h4 class="font-weight-bold">Diplomas Olimpicos</h4>
              <p>Colombia obtuvo un diploma olimpico.</p>
            </div>
            <div class="col-sm-6">
              <i class="flaticon-medal display-2 text-primary"></i>
              <h4 class="font-weight-bold">Medallas</h4>
              <p>Colombia obtuvo dos medallas de plata.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
