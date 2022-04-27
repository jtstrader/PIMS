import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, tap, throwError } from 'rxjs';
import { ICompanyAverageSalary } from '../interfaces/icompany-average-salary';

@Injectable({
  providedIn: 'root'
})
export class CompanyAverageSalaryService {

  constructor(private http: HttpClient) { }
  private url: string = "http://localhost:8080/api/business/avg_salary";

  getTop10(): Observable<ICompanyAverageSalary[]> {
    return this.http.get<String[]>(this.url).pipe(map(result => {
      let ret: ICompanyAverageSalary[] = [];
      for (let x of result) {
        ret.push(
          {company_name: x.split(",")[0], avg_salary: Number(x.split(",")[1])}
        )
      }
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
