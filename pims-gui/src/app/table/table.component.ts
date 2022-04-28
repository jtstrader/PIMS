import { Component, OnInit } from '@angular/core';
import { Subscriber, Subscription } from 'rxjs';
import { IAveragePositionSalaryByBusiness } from '../interfaces/iaverage-position-salary-by-business';
import { ICompanyAverageSalary } from '../interfaces/icompany-average-salary';
import { IDeathRatesByState } from '../interfaces/ideath-rates-by-state';
import { IMaritalCountByState } from '../interfaces/imarital-count-by-state';
import { AveragePositionSalaryByBusinessService } from '../services/average-position-salary-by-business.service';
import { CompanyAverageSalaryService } from '../services/company-average-salary.service';
import { DeathRatesByStateService } from '../services/death-rates-by-state.service';
import { MaritalCountByStateService } from '../services/marital-count-by-state.service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  constructor(private deathRatesByState: DeathRatesByStateService,
              private maritalCountByState: MaritalCountByStateService,
              private companyAverageSalary: CompanyAverageSalaryService,
              private averagePositionSalary: AveragePositionSalaryByBusinessService) { }

  dr_sub!: Subscription;
  mc_sub!: Subscription;
  ca_sub!: Subscription;
  ap_sub!: Subscription;

  table: boolean[] = [false, false, false, false];

  deathRates!: IDeathRatesByState[];
  maritalCount!: IMaritalCountByState[];
  companyAvgSalary!: ICompanyAverageSalary[];
  avgPositionSalary!: IAveragePositionSalaryByBusiness[];
  filteredAvgPositionSalary!: IAveragePositionSalaryByBusiness[];
  errorMessage: string = "";
  
  companies!: String[];

  avgPositionCompanySelection!: string;

  money = new Intl.NumberFormat('en-US', { style:'currency', currency: 'USD' });

  backId: number = 0;
  bckgrdColors: string[] = ["#fff", "#ccc"];

  ngOnInit(): void {
    this.dr_sub = this.deathRatesByState.getDeathRates().subscribe({
      next: drs => this.deathRates = drs,
      error: err => this.errorMessage = err
    });

    this.mc_sub = this.maritalCountByState.getMaritalCount().subscribe({
      next: mc => this.maritalCount = mc,
      error: err => this.errorMessage = err
    });

    this.ca_sub = this.companyAverageSalary.getTop10().subscribe({
      next: ca => this.companyAvgSalary = ca,
      error: err => this.errorMessage = err
    });

    this.ap_sub = this.averagePositionSalary.getAveragePositionSalaries().subscribe({
      next: ap => {
        this.avgPositionSalary = ap;

        this.avgPositionCompanySelection = this.avgPositionSalary[0].company_name;
        this.filteredAvgPositionSalary = this.avgPositionSalary.filter(
          x => x.company_name == this.avgPositionCompanySelection
        );

        this.companies = this.avgPositionSalary.map(x => x.company_name);
      },
      error: err => this.errorMessage = err
    });
  }

  setTable(idx: number): void {
    this.table = this.table.map((_, index) => index == idx ? true : false);
  }

  alternateBackgroundColor(): string {
    return this.bckgrdColors[this.backId == 0 ? this.backId++ : this.backId--]
  }

  // return a string to include trailing zeros
  deathRateAdjust(death_rate: number): string {
    return (death_rate * 100).toFixed(2);
  }

  ngOnDestroy(): void {
    this.dr_sub.unsubscribe();
    this.mc_sub.unsubscribe();
  }
}
