# Electric-Energy-Cehcker
Get the max percentage for each power company in Japan. Please use it to save electricity.

## Usage
Return Type : ```int``` or ```dictionary```

### Values
Enter the value of the power company for which you want to acquire data as an argument.<br>
If you specify ```all```, you can get the data of all electric power companies.

 - 関西電力：```kansai```
 - 中国電力：```chugoku```
 - 東北電力：```tohoku```
 - 四国電力：```shikoku```
 - 九州電力：```kyushu```
 - 中部電力：```chubu```
 - 東京電力：```tokyo```
 - 沖縄電力：```okinawa```
 - 北海道電力：```hokkaido```
 - 北陸電力：```hokuriki```
 - 全電力会社：```all```

### Example Code
```python
from main import get_energy_info

print(get_energy_info('kansai'))
```
