import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SetOutputPathComponent } from './set-output-path.component';

describe('SetOutputPathComponent', () => {
  let component: SetOutputPathComponent;
  let fixture: ComponentFixture<SetOutputPathComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SetOutputPathComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SetOutputPathComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
