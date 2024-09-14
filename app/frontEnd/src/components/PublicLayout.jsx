import Footer from "./Footer";
import Navbar from "./Navbar";

export default function PublicLayout({ children }) {
  return (
    <>
      <button
        type="button"
        class="btn btn-outline-primary back-to-top"
        onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
      >
        <i class="fa fa-angle-double-up"></i>
      </button>
      <Navbar />
      {children}
      <Footer />
    </>
  );
}
