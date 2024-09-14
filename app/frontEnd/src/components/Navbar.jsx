import { Link } from "preact-router/match";

export default function Navbar() {
  return (
    <div class="container-fluid p-0 nav-bar ">
      <nav class="navbar navbar-expand-lg bg-none navbar-dark py-3">
        <a href="" class="navbar-brand">
          <h1 class="m-0 display-4 font-weight-bold text-uppercase text-white">
            Halterofilia - Cauca
          </h1>
        </a>
        <button
          type="button"
          class="navbar-toggler"
          data-toggle="collapse"
          data-target="#navbarCollapse"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div
          class="collapse navbar-collapse justify-content-between"
          id="navbarCollapse"
        >
          <div class="navbar-nav ml-auto p-4 bg-secondary">
            <Link href="/" class="nav-item nav-link active">
              Principal
            </Link>
            <Link href="/about" class="nav-item nav-link">
              Registro Deportistas
            </Link>
            <Link href="/feature" class="nav-item nav-link">
              Logros
            </Link>
            <div class="nav-item dropdown">
              <a
                href="#"
                class="nav-link dropdown-toggle"
                data-toggle="dropdown"
              >
                Menciones
              </a>
              <div class="dropdown-menu text-capitalize">
                <Link href="/blog" class="dropdown-item">
                  Agradecimientos
                </Link>
                <Link href="/single" class="dropdown-item">
                  Noticias
                </Link>
              </div>
            </div>
            <Link href="/contact" class="nav-item nav-link">
              Contacto
            </Link>
          </div>
        </div>
      </nav>
    </div>
  );
}
