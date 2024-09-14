export default function Subscribe() {
  return (
    <div class="subscribe container-fluid my-5 py-5 text-center">
      <h4 class="display-4 text-white font-weight-bold mt-5 mb-3">
        Subscribete A Nuestra Comunidad
      </h4>
      <form class="form-inline justify-content-center mb-5">
        <div class="input-group">
          <input
            type="text"
            class="form-control-lg"
            placeholder="Correo Electronico"
          />
          <div class="input-group-append">
            <button class="btn btn-primary" type="submit">
              Suscribirse
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
