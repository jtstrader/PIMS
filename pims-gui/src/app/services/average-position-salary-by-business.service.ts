import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, throwError } from 'rxjs';
import { IAveragePositionSalaryByBusiness } from '../interfaces/iaverage-position-salary-by-business';

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
          business_name: x.split(",")[0],
          position: x.split(",")[1],
          avg_salary: Number(x.split(",")[2])
        };
      });
      console.log(ret);
      return ret;
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
