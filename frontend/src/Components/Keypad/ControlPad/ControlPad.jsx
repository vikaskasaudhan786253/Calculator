import Button from "../../Button/Button";
import './ControlPad.css'


function ControlPad({ handleClick }) {
    return (
        <div className="control-pad">
            <Button value="AC" onClick={handleClick} />
            <Button value="C" onClick={handleClick} />
            <Button value="⌫" onClick={handleClick} />
            <Button value="(" onClick={handleClick} />
            <Button value=")" onClick={handleClick} />
        </div>
    );
}

export default ControlPad;
