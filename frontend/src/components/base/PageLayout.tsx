import { Layout, PageHeader, PageHeaderProps } from "antd";
// @ts-ignore
import React from "react";
import SlideOver from "../SlideOver/SlideOver";
import Heading from "./Heading/Heading";

interface PageLayoutProps extends PageHeaderProps {
  hasBackButton?: boolean;
  backButton?: React.ReactNode;
}
export const PageLayout = ({
  children,
  hasBackButton,
  backButton,
  ...props
}: PageLayoutProps) => {
  return (
    <div>
      <SlideOver />

      <Heading />
      <PageHeader />

      <div className="mx-10 mt-16">
        <div className="flex items-center justify-between mb-6">
          {props.title ? (
            <h1
              className={hasBackButton ? "font-main mt-20 mx-10" : "font-main"}
            >
              {props.title}
            </h1>
          ) : (
            <h1>{props.title}</h1>
          )}
          <div>{props.extra}</div>
        </div>
        <Layout.Content className="min-h-[calc(100vh-210px)]">
          {children}
        </Layout.Content>
      </div>
    </div>
  );
};
