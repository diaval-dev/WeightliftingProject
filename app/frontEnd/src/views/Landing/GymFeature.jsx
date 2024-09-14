import feature1 from "../../assets/img/feature-1.jpg";
import feature2 from "../../assets/img/feature-2.jpg";
import feature3 from "../../assets/img/feature-3.jpg";
import feature4 from "../../assets/img/feature-4.jpg";

const features_list = [
  {
    title: "Aumento de la fuerza muscular",
    description:
      "Levantar pesas fortalece los músculos al someterlos a cargas progresivas, lo que mejora la capacidad para realizar tareas físicas diarias y aumenta la resistencia física.",
    image: feature1,
  },
  {
    title: "Mejora de la salud ósea",
    description:
      "El entrenamiento con pesas aumenta la densidad ósea, lo que ayuda a prevenir enfermedades como la osteoporosis, especialmente a medida que envejecemos.",
    image: feature2,
  },
  {
    title: "Mejora de la postura y prevención de lesiones",
    description:
      "Al fortalecer los músculos estabilizadores y mejorar el equilibrio, puede corregir desequilibrios musculares, mejorar la postura y el riesgo de lesiones en la vida diaria.",
    image: feature3,
  },
  {
    title: "Aceleración del metabolismo",
    description:
      "Levantar pesas aumenta la masa muscular, lo que, a su vez, acelera el metabolismo. Esto permite que el cuerpo queme más calorías en reposo, favoreciendo la pérdida o el control del peso.",
    image: feature4,
  },
];

export default function GymFeature() {
  return (
    <div class="container feature pt-5">
      <div class="d-flex flex-column text-center mb-5">
        <h4 class="text-primary font-weight-bold">
          Porque entrenar levantamiento de pesas?
        </h4>
        <h4 class="display-4 font-weight-bold">
          Benificios de pertenecer a nuestra LIGA
        </h4>
      </div>
      <div class="row">
        {features_list.map((item, index) => (
          <div key={index} class="col-md-6 mb-5">
            <div class="row align-items-center">
              <div class="col-sm-5">
                <img
                  class="img-fluid mb-3 mb-sm-0"
                  src={item.image}
                  alt="Image"
                />
                <i class="flaticon-barbell"></i>
              </div>
              <div class="col-sm-7">
                <h4 class="font-weight-bold">{item.title}</h4>
                <p>{item.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
