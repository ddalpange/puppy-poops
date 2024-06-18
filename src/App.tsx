import React, { Suspense, useState } from "react";

import scene1 from "./images/scene1.png";
import scene10 from "./images/scene10.png";
import scene11 from "./images/scene11.png";
import scene12 from "./images/scene12.png";
import scene13 from "./images/scene13.png";
import scene14 from "./images/scene14.png";
import scene2 from "./images/scene2.png";
import scene3 from "./images/scene3.png";
import scene4 from "./images/scene4.png";
import scene5 from "./images/scene5.png";
import scene6 from "./images/scene6.png";
import scene7 from "./images/scene7.png";
import scene8 from "./images/scene8.png";
import scene9 from "./images/scene9.png";

const images = [
  scene1,
  scene2,
  scene3,
  scene4,
  scene5,
  scene6,
  scene7,
  scene8,
  scene9,
  scene10,
  scene11,
  scene12,
  scene13,
  scene14,
];

const App: React.FC = () => {
  const [idx, setIdx] = useState(0);

  return (
    <Suspense>
      <img
        alt=""
        onClick={() => setIdx((pv) => (pv === images.length - 1 ? 0 : ++pv))}
        src={images[idx]}
      ></img>
    </Suspense>
  );
};

export default App;
