import NumberPad from "./NumberPad/NumberPad";
import OperatorPad from "./OperatorPad/OperatorPad";

import "./MainPad.css";

function MainPad({ handleClick }) {
    return (
        <div className="main-pad">
            <NumberPad handleClick={handleClick} />
            <OperatorPad handleClick={handleClick} />
        </div>
    );
}

export default MainPad;
