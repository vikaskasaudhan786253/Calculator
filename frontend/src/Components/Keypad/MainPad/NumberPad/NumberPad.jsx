import Button from "../../../Button/Button";
import './NumberPad.css'

function NumberPad ({handleClick}){
    return(

        <div className="number-pad">
            <Button value="7" onClick={handleClick} />
            <Button value="8" onClick={handleClick} />
            <Button value="9" onClick={handleClick} />

            <Button value="4" onClick={handleClick} />
            <Button value="5" onClick={handleClick} />
            <Button value="6" onClick={handleClick} />

            <Button value="1" onClick={handleClick} />
            <Button value="2" onClick={handleClick} />
            <Button value="3" onClick={handleClick} />

            <Button value="0" onClick={handleClick} />
            <Button value="." onClick={handleClick} />
        </div>
    )
}
export default NumberPad
