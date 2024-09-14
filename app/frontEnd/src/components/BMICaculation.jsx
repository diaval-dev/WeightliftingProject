export default function BMICaculation() {
  return (
    <div class="container-fluid position-relative bmi my-5">
      <div class="container">
        <div class="row px-3 align-items-center">
          <div class="col-md-6">
            <div class="pr-md-3 d-none d-md-block">
              <h4 class="text-primary">Indice De Masa Corporal </h4>
              <h4 class="display-4 text-white font-weight-bold mb-4">
                Cual es tu BMI?
              </h4>
              <p class="m-0 text-white">
                {" "}
                El BMI mide tu grasa corporal, usando tu peso y estatura para
                calcular tu Índice de masa corporal. Este número puede ayudarte
                a determinar si tienes algún problema con tu peso.
              </p>
            </div>
          </div>
          <div class="col-md-6 bg-secondary py-5">
            <div class="py-5 px-3">
              <h1 class="mb-4 text-white">Calcula tu BMI</h1>
              <form>
                <div class="form-row">
                  <div class="col form-group">
                    <input
                      type="text"
                      class="form-control form-control-lg bg-dark text-white"
                      placeholder="Peso (KG)"
                    />
                  </div>
                  <div class="col form-group">
                    <input
                      type="text"
                      class="form-control form-control-lg bg-dark text-white"
                      placeholder="Altura (CM)"
                    />
                  </div>
                </div>
                <div class="form-row">
                  <div class="col form-group">
                    <input
                      type="text"
                      class="form-control form-control-lg bg-dark text-white"
                      placeholder="Edad"
                    />
                  </div>
                  <div class="col form-group">
                    <select class="custom-select custom-select-lg bg-dark text-muted">
                      <option>Genero</option>
                      <option>Maculino</option>
                      <option>Femenino</option>
                    </select>
                  </div>
                </div>
                <div class="form-row">
                  <div class="col">
                    <input
                      type="button"
                      class="btn btn-lg btn-block btn-dark border-light"
                      value="Calcular Ahora"
                    />
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
