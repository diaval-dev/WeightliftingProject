import Carousel from "../../components/Carousel";

import AboutStart from "./AboutStart";
import GymaCLass from "./GymaCLass";
import Feature from "./Feature";
import GymFeature from "./GymFeature";
import Subscribe from "./Subscribe";
import ClassTimeTable from "./ClassTimeTable";
import BMICaculation from "../../components/BMICaculation";
import PublicLayout from "../../components/PublicLayout";

export default function Landing() {
  return (
    <PublicLayout>
      <Carousel />

      <GymaCLass />
      <AboutStart />
      <Feature />
      <GymFeature />
      <Subscribe />
      <ClassTimeTable />
      <BMICaculation />
    </PublicLayout>
  );
}
