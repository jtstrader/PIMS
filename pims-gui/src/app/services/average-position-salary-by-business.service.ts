import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, throwError } from 'rxjs';
import { IAveragePositionSalaryByBusiness } from '../interfaces/iaverage-position-salary-by-business';
import { IPositionSalariesFormatted } from '../interfaces/iposition-salaries-formatted';

@Injectable({
  providedIn: 'root'
})
export class AveragePositionSalaryByBusinessService {

  constructor(private http: HttpClient) { }
  private url: string = "http://localhost:8080/api/occupation/position_salaries"

  getAveragePositionSalaries(): Observable<IAveragePositionSalaryByBusiness[]> {
    // sample result: ["FL, 0.160220", "GA, 0.039402"]
    return this.http.get<String[]>(this.url).pipe(map(result => {
      let ret: IAveragePositionSalaryByBusiness[] = result.map(x => {
        return {
          company_name: x.split(",")[0],
          position: x.split(",")[1],
          avg_salary: Number(x.split(",")[2])
        };
      });
      console.log(ret);
      return ret;
    }),
    catchError(this.handleError));
  }

  getAveragePositionSalariesFMT(): Observable<IPositionSalariesFormatted[]> {
    return this.http.get<String[]>(this.url).pipe(map(result => {
      let ret: IAveragePositionSalaryByBusiness[] = result.map(x => {
        return {
          company_name: x.split(",")[0],
          position: x.split(",")[1],
          avg_salary: Number(x.split(",")[2])
        };
      });
      let arrFmt: IPositionSalariesFormatted[] = [];
      ret.forEach(e => {
        const obj: IPositionSalariesFormatted = {
          name: e.position,
          series: [
            {
              name: e.company_name,
              value: e.avg_salary
            }
          ]
        }
        if(!arrFmt.some(o => o.name === e.position))
        {
          arrFmt.push(obj);
        }
        else
        {
          arrFmt.find(o => o.name === e.position)?.series.push(obj.series[0]);
        }
      })
      console.log(ret);
      return arrFmt;
    }),
    catchError(this.handleError));
  }

  private handleError(err: HttpErrorResponse) {
    let errorMessage = '';
    if (err.error instanceof ErrorEvent) {
      errorMessage = `An error occured: ${err.error.message}`;
    } else {
      errorMessage = `Server returned code: ${err.status}, error message is: ${err.message}`;
    }
    return throwError(() => errorMessage);
  }
}
