import Button from "../../../Button/Button";
import './OperatorPad.css'

function OperatorPad({ handleClick }) {
    return (
        <div className="operator-pad">
            <Button value="/" onClick={handleClick} />
            <Button value="*" onClick={handleClick} />
            <Button value="-" onClick={handleClick} />
            <Button value="+" onClick={handleClick} />
            <Button value="%" onClick={handleClick} />
        </div>
    );
}

export default OperatorPad;
